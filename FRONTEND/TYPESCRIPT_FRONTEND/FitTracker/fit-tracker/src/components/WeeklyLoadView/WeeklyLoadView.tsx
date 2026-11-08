import type { WeeklyLoad } from "../../types/weeklyLoad";
import type { RestRecommendation } from "../../types/restRecommendation";
import "./WeeklyLoadView.css";

type WeeklyLoadViewProps = {
  weeklyLoad: WeeklyLoad;
  restRecommendation: RestRecommendation;
};

export const WeeklyLoadView = ({
  weeklyLoad,
  restRecommendation,
}: WeeklyLoadViewProps) => {
  return (
    <section className="weekly-load-view card">
      <h2>Carga semanal</h2>

      <p>Total de minutos: {weeklyLoad.totalMinutes} min</p>

      <p>Total de calorías: {weeklyLoad.totalCalories} kcal</p>

      <h3>Distribución por categoría</h3>

      <p>Cardio: {weeklyLoad.cardioMinutes} min</p>

      <p>Fuerza: {weeklyLoad.strengthMinutes} min</p>

      <p>Flexibilidad: {weeklyLoad.flexibilityMinutes} min</p>

      <p>Días entrenados: {weeklyLoad.trainingDays}</p>

      <h3>Recomendación de descanso</h3>

      {restRecommendation === "high" && (
        <p>
          Estás entrenando con una carga elevada. Considera incorporar más
          descanso.
        </p>
      )}

      {restRecommendation === "low" && (
        <p>
          Tu actividad semanal es baja. Considera agregar días o minutos de
          entrenamiento.
        </p>
      )}

      {restRecommendation === "balanced" && (
        <p>Tu carga semanal está dentro del rango establecido.</p>
      )}
    </section>
  );
};
