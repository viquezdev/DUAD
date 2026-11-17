import { useState } from "react";
import type { Instructor } from "../../types/instructor";
import type { User } from "../../types/user";
import { getInstructorWeeklySummaries } from "../../utils/fitness";
import type { InstructorId } from "../../types/instructorId";
import "./InstructorView.css";

interface InstructorViewProps {
  instructors: Instructor[];
  users: User[];
}

export function InstructorView({ instructors, users }: InstructorViewProps) {
  const [selectedInstructorId, setSelectedInstructorId] =
    useState<InstructorId | null>(null);

  const selectedInstructor =
    instructors.find((instructor) => instructor.id === selectedInstructorId) ??
    null;

  const weeklySummaries = selectedInstructor
    ? getInstructorWeeklySummaries(selectedInstructor, users)
    : [];

  return (
    <section className="instructor-view">
      <h2>Panel de instructores</h2>

      <label htmlFor="instructor-select">Seleccionar instructor:</label>

      <select
        id="instructor-select"
        value={selectedInstructorId ?? ""}
        onChange={(e) =>
          setSelectedInstructorId(
            e.target.value === "" ? null : Number(e.target.value),
          )
        }
      >
        <option value={0}>Seleccione un instructor</option>

        {instructors.map((instructor) => (
          <option key={instructor.id} value={instructor.id}>
            {instructor.name}
          </option>
        ))}
      </select>

      {selectedInstructor && (
        <div className="assigned-users">
          <h3>Instructor: {selectedInstructor.name}</h3>

          {weeklySummaries.length === 0 ? (
            <p>Este instructor todavía no tiene usuarios asignados.</p>
          ) : (
            weeklySummaries.map((summary) => (
              <article key={summary.userId} className="user-summary">
                <h4>
                  {summary.name} ({summary.experienceLevel}){" "}
                </h4>

                <p>Rutina: {summary.routineName ?? "Sin rutina asignada"}</p>

                <div className="weekly-summary">
                  <h5>Resumen semanal</h5>

                  <p>Días de entrenamiento: {summary.trainingDays}</p>

                  <p>Minutos totales: {summary.totalMinutes}</p>

                  <p>Calorías totales: {summary.totalCalories}</p>

                  <div className="pending-exercises">
                    <p>
                      Ejercicios pendientes: {summary.pendingExercises.length}
                    </p>

                    {summary.pendingExercises.length > 0 ? (
                      <ul>
                        {summary.pendingExercises.map((exercise) => (
                          <li key={exercise.id}>{exercise.name}</li>
                        ))}
                      </ul>
                    ) : (
                      <p>No hay ejercicios pendientes.</p>
                    )}
                  </div>

                  {summary.restRecommendation === "low" && (
                    <p>
                      Recomendación de descanso: Tu actividad semanal es baja.
                      Considera agregar días o minutos de entrenamiento.
                    </p>
                  )}
                  {summary.restRecommendation === "balanced" && (
                    <p>
                      Recomendación de descanso: Tu carga semanal está dentro
                      del rango establecido.
                    </p>
                  )}
                  {summary.restRecommendation === "high" && (
                    <p>
                      Recomendación de descanso: Estás entrenando con una carga
                      elevada. Considera incorporar más descanso.
                    </p>
                  )}
                </div>
              </article>
            ))
          )}
        </div>
      )}
    </section>
  );
}
