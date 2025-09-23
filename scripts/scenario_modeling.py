"""
Сценарное моделирование для выбора модели монетизации
Основано на документе decision.md

Реализует 4 модели монетизации:
A: Freemium + Premium подписка
B: Subscription-only с trial
C: Pay-per-use + подписка
D: Freemium + комиссия с доставки

Для каждой модели рассчитывается 3 сценария (базовый, худший, лучший)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
import warnings
import os

warnings.filterwarnings("ignore")

# Устанавливаем русские шрифты для matplotlib
plt.rcParams["font.family"] = "DejaVu Sans"

# Определяем пути для сохранения результатов
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SOURCE_DIR = os.path.join(PROJECT_ROOT, "source")

# Создаем папку source если её нет
os.makedirs(SOURCE_DIR, exist_ok=True)


class MonetizationScenarioModeling:

    def __init__(self):
        # Константы из документа
        self.MRS_MRR_THRESHOLD = 35000  # $35K MRR
        self.MRS_LTV_CAC_THRESHOLD = 3.0  # 3:1 LTV:CAC ratio
        self.RED_LTV_CAC_THRESHOLD = 2.0  # <2:1 красная зона
        self.YELLOW_LTV_CAC_THRESHOLD = 3.0  # 2:1-3:1 желтая зона

        # Базовые диапазоны параметров
        self.parameter_ranges = {
            # Рыночные факторы
            "market_size": (500000, 2000000),  # потенциальные пользователи
            "willingness_to_pay_ratio": (0.15, 0.45),  # % от TAM готовых платить
            # Конкурентные факторы
            "competitors_count": (0, 5),
            "cac_base": (10, 50),  # базовый CAC в долларах
            # Продуктовые факторы
            "conversion_rate": (0.01, 0.10),  # 1%-10%
            "churn_rate_monthly": (0.05, 0.25),  # 5%-25% в месяц
            "arpu_base": (5, 25),  # $5-25 в месяц
            # Внешние факторы
            "economic_multiplier": (0.7, 1.3),  # влияние экономики
            "delivery_commission": (0.0, 0.03),  # 0-3% комиссии с доставки
        }

        # Параметры моделей монетизации
        self.models = {
            "A": {  # Freemium + Premium
                "name": "Freemium + Premium подписка",
                "arpu_multiplier": 1.0,
                "conversion_multiplier": 0.8,  # ниже из-за freemium
                "cac_multiplier": 0.7,  # дешевле привлечение
                "churn_multiplier": 1.2,  # выше отток
            },
            "B": {  # Subscription-only с trial
                "name": "Subscription-only с trial",
                "arpu_multiplier": 1.3,  # выше ARPU
                "conversion_multiplier": 1.2,  # выше конверсия после trial
                "cac_multiplier": 1.1,  # дороже привлечение
                "churn_multiplier": 0.9,  # ниже отток
            },
            "C": {  # Pay-per-use + подписка
                "name": "Pay-per-use + подписка",
                "arpu_multiplier": 0.9,  # ниже ARPU
                "conversion_multiplier": 1.1,  # легче начать платить
                "cac_multiplier": 0.9,  # средний CAC
                "churn_multiplier": 1.0,  # средний отток
            },
            "D": {  # Freemium + комиссия
                "name": "Freemium + комиссия с доставки",
                "arpu_multiplier": 0.6,  # низкий прямой ARPU
                "conversion_multiplier": 0.5,  # меньше прямых платежей
                "cac_multiplier": 0.6,  # дешевое привлечение
                "churn_multiplier": 1.1,  # средний отток
                "has_commission": True,  # дополнительная выручка с комиссии
            },
        }

    def generate_scenario_params(
        self, scenario: str, n_iterations: int = 10000
    ) -> Dict:
        """
        Генерирует параметры для заданного сценария

        scenario: 'base', 'worst', 'best'
        """
        params = {}

        for param_name, (min_val, max_val) in self.parameter_ranges.items():
            if scenario == "base":
                # Равномерное распределение по всему диапазону
                params[param_name] = np.random.uniform(min_val, max_val, n_iterations)
            elif scenario == "worst":
                # Смещение к нижней границе (75% веса в нижней половине)
                lower_half = np.random.uniform(
                    min_val, (min_val + max_val) / 2, int(n_iterations * 0.75)
                )
                upper_half = np.random.uniform(
                    (min_val + max_val) / 2, max_val, int(n_iterations * 0.25)
                )
                params[param_name] = np.concatenate([lower_half, upper_half])
                np.random.shuffle(params[param_name])
            elif scenario == "best":
                # Смещение к верхней границе (75% веса в верхней половине)
                lower_half = np.random.uniform(
                    min_val, (min_val + max_val) / 2, int(n_iterations * 0.25)
                )
                upper_half = np.random.uniform(
                    (min_val + max_val) / 2, max_val, int(n_iterations * 0.75)
                )
                params[param_name] = np.concatenate([lower_half, upper_half])
                np.random.shuffle(params[param_name])

        return params

    def calculate_metrics(self, params: Dict, model_key: str, months: int = 24) -> Dict:
        """
        Рассчитывает метрики для заданной модели и параметров
        """
        model = self.models[model_key]
        n_iterations = len(params["market_size"])

        # Расчет базовых метрик для каждой итерации
        results = {
            "total_users": [],
            "paying_users": [],
            "mrr": [],
            "ltv": [],
            "cac": [],
            "ltv_cac_ratio": [],
            "commission_revenue": [],
        }

        for i in range(n_iterations):
            # Общее количество пользователей
            total_users = (
                params["market_size"][i]
                * params["willingness_to_pay_ratio"][i]
                * params["economic_multiplier"][i]
            )

            # Корректировка на конкуренцию (простая модель)
            competition_factor = max(0.3, 1 - params["competitors_count"][i] * 0.15)
            total_users *= competition_factor

            # ARPU с учетом модели
            arpu = (
                params["arpu_base"][i]
                * model["arpu_multiplier"]
                * params["economic_multiplier"][i]
            )

            # Conversion rate с учетом модели
            conversion = params["conversion_rate"][i] * model["conversion_multiplier"]
            paying_users = total_users * conversion

            # Churn rate с учетом модели
            churn_rate = params["churn_rate_monthly"][i] * model["churn_multiplier"]

            # CAC с учетом модели
            cac = (
                params["cac_base"][i]
                * model["cac_multiplier"]
                * (1 + params["competitors_count"][i] * 0.1)
            )

            # MRR (учитываем снижение из-за churn)
            retention_factor = (1 - churn_rate) ** months
            mrr = paying_users * arpu * retention_factor

            # LTV
            if churn_rate > 0:
                ltv = arpu / churn_rate * 0.7  # 70% margin
            else:
                ltv = arpu * 24 * 0.7  # если churn=0, берем 24 месяца

            # LTV:CAC ratio
            ltv_cac_ratio = ltv / cac if cac > 0 else 0

            # Дополнительная выручка с комиссии (только для модели D)
            commission_revenue = 0
            if model.get("has_commission", False):
                # Предполагаем, что каждый пользователь делает заказы на $50/месяц
                avg_order_value = 50
                orders_per_user_month = 2
                commission_revenue = (
                    total_users
                    * avg_order_value
                    * orders_per_user_month
                    * params["delivery_commission"][i]
                    * 12
                )  # годовая

            results["total_users"].append(total_users)
            results["paying_users"].append(paying_users)
            results["mrr"].append(mrr)
            results["ltv"].append(ltv)
            results["cac"].append(cac)
            results["ltv_cac_ratio"].append(ltv_cac_ratio)
            results["commission_revenue"].append(commission_revenue)

        return results

    def analyze_results(self, results: Dict, model_name: str, scenario: str) -> Dict:
        """
        Анализирует результаты моделирования
        """
        mrr_array = np.array(results["mrr"])
        ltv_cac_array = np.array(results["ltv_cac_ratio"])

        # Вероятность достижения MRS
        mrs_achieved = (mrr_array >= self.MRS_MRR_THRESHOLD) & (
            ltv_cac_array >= self.MRS_LTV_CAC_THRESHOLD
        )
        prob_mrs = np.mean(mrs_achieved)

        # Guardrails анализ
        red_zone = ltv_cac_array < self.RED_LTV_CAC_THRESHOLD
        yellow_zone = (ltv_cac_array >= self.RED_LTV_CAC_THRESHOLD) & (
            ltv_cac_array < self.YELLOW_LTV_CAC_THRESHOLD
        )
        green_zone = ltv_cac_array >= self.YELLOW_LTV_CAC_THRESHOLD

        prob_red = np.mean(red_zone)
        prob_yellow = np.mean(yellow_zone)
        prob_green = np.mean(green_zone)

        # Процентили MRR
        mrr_percentiles = {
            "10%": np.percentile(mrr_array, 10),
            "50%": np.percentile(mrr_array, 50),
            "90%": np.percentile(mrr_array, 90),
        }

        # Доверительные интервалы LTV:CAC
        ltv_cac_ci = {
            "5%": np.percentile(ltv_cac_array, 5),
            "50%": np.percentile(ltv_cac_array, 50),
            "95%": np.percentile(ltv_cac_array, 95),
        }

        return {
            "model": model_name,
            "scenario": scenario,
            "prob_mrs_achieved": prob_mrs,
            "prob_red_zone": prob_red,
            "prob_yellow_zone": prob_yellow,
            "prob_green_zone": prob_green,
            "mrr_percentiles": mrr_percentiles,
            "ltv_cac_ci": ltv_cac_ci,
            "avg_mrr": np.mean(mrr_array),
            "avg_ltv_cac": np.mean(ltv_cac_array),
            "total_commission_revenue": (
                np.mean(results["commission_revenue"])
                if results["commission_revenue"]
                else 0
            ),
        }

    def run_full_simulation(self, n_iterations: int = 10000) -> pd.DataFrame:
        """
        Запускает полное моделирование для всех моделей и сценариев
        """
        all_results = []

        scenarios = ["worst", "base", "best"]

        for scenario in scenarios:
            print(f"Запуск сценария: {scenario}")
            params = self.generate_scenario_params(scenario, n_iterations)

            for model_key in self.models.keys():
                model_name = self.models[model_key]["name"]
                print(f"  Модель {model_key}: {model_name}")

                # Расчет метрик
                metrics = self.calculate_metrics(params, model_key)

                # Анализ результатов
                analysis = self.analyze_results(metrics, model_name, scenario)
                all_results.append(analysis)

        return pd.DataFrame(all_results)

    def create_visualizations(self, results_df: pd.DataFrame):
        """
        Создает визуализации результатов моделирования
        """
        # Настройка стиля
        plt.style.use("seaborn-v0_8")
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle(
            "Результаты сценарного моделирования монетизации",
            fontsize=16,
            fontweight="bold",
        )

        # 1. Вероятность достижения MRS по моделям и сценариям
        ax1 = axes[0, 0]
        mrs_pivot = results_df.pivot(
            index="model", columns="scenario", values="prob_mrs_achieved"
        )
        mrs_pivot.plot(kind="bar", ax=ax1, width=0.8)
        ax1.set_title("Вероятность достижения MRS")
        ax1.set_ylabel("Вероятность")
        ax1.legend(title="Сценарий")
        ax1.tick_params(axis="x", rotation=45)

        # 2. Средний MRR по моделям
        ax2 = axes[0, 1]
        mrr_pivot = results_df.pivot(
            index="model", columns="scenario", values="avg_mrr"
        )
        mrr_pivot.plot(kind="bar", ax=ax2, width=0.8)
        ax2.set_title("Средний MRR ($)")
        ax2.set_ylabel("MRR ($)")
        ax2.axhline(
            y=self.MRS_MRR_THRESHOLD, color="red", linestyle="--", label="MRS порог"
        )
        ax2.legend(title="Сценарий")
        ax2.tick_params(axis="x", rotation=45)

        # 3. Средний LTV:CAC ratio
        ax3 = axes[1, 0]
        ltv_cac_pivot = results_df.pivot(
            index="model", columns="scenario", values="avg_ltv_cac"
        )
        ltv_cac_pivot.plot(kind="bar", ax=ax3, width=0.8)
        ax3.set_title("Средний LTV:CAC ratio")
        ax3.set_ylabel("LTV:CAC")
        ax3.axhline(
            y=self.MRS_LTV_CAC_THRESHOLD,
            color="green",
            linestyle="--",
            label="MRS порог",
        )
        ax3.axhline(
            y=self.RED_LTV_CAC_THRESHOLD,
            color="red",
            linestyle="--",
            label="Красная зона",
        )
        ax3.legend(title="Сценарий")
        ax3.tick_params(axis="x", rotation=45)

        # 4. Распределение по зонам guardrails
        ax4 = axes[1, 1]
        base_scenario = results_df[results_df["scenario"] == "base"]
        guardrails_data = base_scenario[
            ["model", "prob_red_zone", "prob_yellow_zone", "prob_green_zone"]
        ].set_index("model")
        guardrails_data.plot(
            kind="bar",
            stacked=True,
            ax=ax4,
            color=["red", "yellow", "green"],
            alpha=0.7,
            width=0.8,
        )
        ax4.set_title("Распределение по зонам (базовый сценарий)")
        ax4.set_ylabel("Вероятность")
        ax4.legend(["Красная", "Желтая", "Зеленая"])
        ax4.tick_params(axis="x", rotation=45)

        plt.tight_layout()
        # Сохраняем в папку source
        output_path = os.path.join(SOURCE_DIR, "monetization_analysis.png")
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.show()

    def print_detailed_results(self, results_df: pd.DataFrame):
        """
        Выводит детальные результаты анализа
        """
        print("\n" + "=" * 80)
        print("ДЕТАЛЬНЫЕ РЕЗУЛЬТАТЫ СЦЕНАРНОГО МОДЕЛИРОВАНИЯ")
        print("=" * 80)

        for scenario in ["worst", "base", "best"]:
            scenario_data = results_df[results_df["scenario"] == scenario]
            scenario_names = {"worst": "ХУДШИЙ", "base": "БАЗОВЫЙ", "best": "ЛУЧШИЙ"}

            print(f"\n{scenario_names[scenario]} СЦЕНАРИЙ:")
            print("-" * 50)

            # Сортируем по вероятности достижения MRS
            scenario_data = scenario_data.sort_values(
                "prob_mrs_achieved", ascending=False
            )

            for _, row in scenario_data.iterrows():
                model_short = row["model"].split(":")[0]  # Берем короткое название
                print(f"\n{model_short}:")
                print(f"  Вероятность MRS: {row['prob_mrs_achieved']:.1%}")
                print(f"  Средний MRR: ${row['avg_mrr']:,.0f}")
                print(f"  Средний LTV:CAC: {row['avg_ltv_cac']:.2f}")
                print(
                    f"  Зоны: Красная {row['prob_red_zone']:.1%} | "
                    f"Желтая {row['prob_yellow_zone']:.1%} | "
                    f"Зеленая {row['prob_green_zone']:.1%}"
                )

                if row["total_commission_revenue"] > 0:
                    print(
                        f"  Доп. выручка с комиссии: ${row['total_commission_revenue']:,.0f}/год"
                    )

        # Рекомендации
        print("\n" + "=" * 80)
        print("РЕКОМЕНДАЦИИ НА ОСНОВЕ МОДЕЛИРОВАНИЯ:")
        print("=" * 80)

        # Лучшая модель по базовому сценарию
        base_scenario = results_df[results_df["scenario"] == "base"]
        best_model = base_scenario.loc[base_scenario["prob_mrs_achieved"].idxmax()]

        print(f"\n1. РЕКОМЕНДУЕМАЯ МОДЕЛЬ: {best_model['model']}")
        print(f"   Вероятность достижения MRS: {best_model['prob_mrs_achieved']:.1%}")
        print(f"   Устойчивость к рискам: {1 - best_model['prob_red_zone']:.1%}")

        # Анализ рисков
        risky_models = base_scenario[base_scenario["prob_red_zone"] > 0.3]
        if not risky_models.empty:
            print(f"\n2. РИСКОВАННЫЕ МОДЕЛИ (>30% красной зоны):")
            for _, model in risky_models.iterrows():
                print(
                    f"   - {model['model']}: {model['prob_red_zone']:.1%} вероятность провала"
                )

        # Консервативные модели
        safe_models = base_scenario[base_scenario["prob_green_zone"] > 0.5]
        if not safe_models.empty:
            print(f"\n3. КОНСЕРВАТИВНЫЕ МОДЕЛИ (>50% зеленой зоны):")
            for _, model in safe_models.iterrows():
                print(
                    f"   - {model['model']}: {model['prob_green_zone']:.1%} зеленая зона"
                )


def main():
    """
    Основная функция для запуска моделирования
    """
    print("Запуск сценарного моделирования монетизации...")
    print("Параметры: 10,000 итераций, 4 модели, 3 сценария")
    print("-" * 60)

    # Создаем экземпляр модели
    modeling = MonetizationScenarioModeling()

    # Запускаем полное моделирование
    results_df = modeling.run_full_simulation(n_iterations=10000)

    # Выводим результаты
    modeling.print_detailed_results(results_df)

    # Создаем визуализации
    print("\nСоздание визуализаций...")
    modeling.create_visualizations(results_df)

    # Сохраняем результаты в CSV в папку source
    output_csv_path = os.path.join(SOURCE_DIR, "monetization_results.csv")
    results_df.to_csv(output_csv_path, index=False)

    print(f"\nРезультаты сохранены в файл: {output_csv_path}")
    print(
        f"Графики сохранены в файл: {os.path.join(SOURCE_DIR, 'monetization_analysis.png')}"
    )

    return results_df


if __name__ == "__main__":
    results = main()