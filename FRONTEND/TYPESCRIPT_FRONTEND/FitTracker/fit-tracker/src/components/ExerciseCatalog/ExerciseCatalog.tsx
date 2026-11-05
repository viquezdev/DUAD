import type { Exercise } from "../../types/exercise";
import type { CompleteProfile } from "../../types/completeProfile";
import { getExerciseCatalog } from "../../utils/exerciseCatalog";
import { describeExercise } from "../../utils/exerciseDescription";
import "./ExerciseCatalog.css";

interface ExerciseCatalogProps {
  exercises: Exercise[];
  profile: CompleteProfile;
}

export const ExerciseCatalog = ({
  exercises,
  profile,
}: ExerciseCatalogProps) => {
  const catalog = getExerciseCatalog(exercises);
  const totalCardio =
    catalog.find((summary) => summary.category === "cardio")?.exercises
      .length ?? 0;

  const totalStrength =
    catalog.find((summary) => summary.category === "strength")?.exercises
      .length ?? 0;

  const totalFlexibility =
    catalog.find((summary) => summary.category === "flexibility")?.exercises
      .length ?? 0;

  return (
    <div className="catalog">
      <h2>Catálogo de Ejercicios</h2>
      <div className="exercise-counter">
        <h3>Resumen por categoría</h3>
        <p>Cardio: {totalCardio} ejercicios</p>
        <p>Fuerza: {totalStrength} ejercicios</p>
        <p>Flexibilidad: {totalFlexibility} ejercicios</p>
        <p>Total registrados: {exercises.length} ejercicios</p>
      </div>

      {catalog.map((summary) => (
        <section className="catalog-category" key={summary.category}>
          <h3>
            {summary.category === "cardio" && "Cardio"}
            {summary.category === "strength" && "Fuerza"}
            {summary.category === "flexibility" && "Flexibilidad"} (
            {summary.exercises.length} ejercicios, {summary.totalMinutes} min,{" "}
            {summary.totalCalories} kcal)
          </h3>

          {summary.exercises.length > 0 ? (
            <ul>
              {summary.exercises.map((exercise) => (
                <li key={exercise.id}>{describeExercise(exercise)}</li>
              ))}
            </ul>
          ) : (
            <p>No hay ejercicios en esta categoría.</p>
          )}
        </section>
      ))}

      <p className="catalog-total">Total: {exercises.length} ejercicios</p>

      <section className="catalog-profile">
        <h2>Perfil del usuario</h2>
        <p>
          Usuario: {profile.name} | Nivel: {profile.experienceLevel} |
          Membresía: {profile.membershipPlan}
        </p>
      </section>
    </div>
  );
};

export default ExerciseCatalog;
