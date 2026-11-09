import { UserForm } from "./components/UserForm/UserForm";
import type { UserFormData } from "./components/UserForm/UserForm";
import { useState } from "react";
import { ExerciseForm } from "./components/ExerciseForm/ExerciseForm";
import type { Exercise, NewExercise } from "./types/exercise";
import type { WeeklyRoutine } from "./types/weeklyRoutine";
import type { DayOfWeek } from "./types/routineEntry";
import type { RoutineExercise } from "./types/routineExercise";
import { RoutineView } from "./components/RoutineView/RoutineView";
import { WeeklyLoadView } from "./components/WeeklyLoadView/WeeklyLoadView";

import {
  calculateCalories,
  formatDuration,
  calculatePace,
  findLongestExercise,
  findHighestCalorieExercise,
  calculateCaloriePercentage,
  calculateWeeklyLoad,
  getRestRecommendation,
  // calculateAverageCalories,
  //  calculateTotalCalories,
  // findHighestCalorieDay,
} from "./utils/fitness";
import { RoutineForm } from "./components/RoutineForm/RoutineForm";
import type { User } from "./types/user";
import { ExerciseCatalog } from "./components/ExerciseCatalog/ExerciseCatalog";
import "./App.css";

function App() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUserId, setSelectedUserId] = useState<User["id"] | null>(null);
  const selectedUser = users.find((user) => user.id === selectedUserId) || null;
  const handleUserSubmit = (data: UserFormData) => {
    const newUserId = users.length + 1;
    setUsers((currentUsers) => [
      ...currentUsers,
      {
        id: newUserId,
        name: data.name,
        age: data.age,
        email: data.email,
        experienceLevel: data.experienceLevel,
        membershipPlan: data.membershipPlan,
        startDate: data.startDate,
        isActive: data.isActive,
      },
    ]);
    setSelectedUserId(newUserId);
  };
  const handleExerciseSubmit = (data: NewExercise) => {
    const nextId =
      exercises.length === 0
        ? 1
        : Math.max(...exercises.map((exercise) => exercise.id)) + 1;

    const newExercise: Exercise = {
      ...data,
      id: nextId,
    };

    setExercises((currentExercises) => [...currentExercises, newExercise]);
  };
  const handleRoutineCreate = (newRoutine: WeeklyRoutine) => {
    if (selectedUserId === null) {
      return;
    }

    setUsers((currentUsers) =>
      currentUsers.map((user) =>
        user.id === selectedUserId ? { ...user, routine: newRoutine } : user,
      ),
    );
  };
  const handleToggleExercise = (
    day: DayOfWeek,
    exerciseId: RoutineExercise["id"],
  ) => {
    if (selectedUserId === null) {
      return;
    }

    setUsers((currentUsers) =>
      currentUsers.map((user) => {
        if (user.id !== selectedUserId || !user.routine) {
          return user;
        }

        return {
          ...user,
          routine: {
            ...user.routine,
            sessions: user.routine.sessions.map((session) => {
              if (session.day !== day) {
                return session;
              }

              return {
                ...session,
                exercises: session.exercises.map((exercise) =>
                  exercise.id === exerciseId
                    ? {
                        ...exercise,
                        isCompleted: !exercise.isCompleted,
                      }
                    : exercise,
                ),
              };
            }),
          },
        };
      }),
    );
  };
  const longestExercise = findLongestExercise(exercises);
  const highestCalorieExercise = findHighestCalorieExercise(exercises);
  const totalCalories = exercises.reduce(
    (total, exercise) => total + calculateCalories(exercise),
    0,
  );
  const weeklyLoad = selectedUser?.routine
    ? calculateWeeklyLoad(selectedUser.routine)
    : null;
  const restRecommendation = weeklyLoad
    ? getRestRecommendation(weeklyLoad)
    : null;
  //const highestCalorieDay = routine ? findHighestCalorieDay(routine) : null;
  return (
    <>
      <header className="app-header">
        <h1>FitTracker</h1>
        <p>Seguimiento de tu entrenamiento</p>
      </header>
      <div className="App">
        <div className="forms-container">
          <div className="column-heading">
            <h2>Administración</h2>
            <p>Gestión general de FitTracker</p>
          </div>
          <UserForm onSubmit={handleUserSubmit} />

          <ExerciseForm onSubmit={handleExerciseSubmit} />
          <section className="card">
            <h2>Ejercicios registrados</h2>
            {exercises.map((exercise) => {
              const pace = calculatePace(exercise);
              return (
                <p key={exercise.id}>
                  {exercise.name} - {formatDuration(exercise.duration)} -{" "}
                  {calculateCalories(exercise)} cal
                  {pace !== null ? ` - Pace: ${pace} min/km` : ""}
                </p>
              );
            })}
            <p>Total de calorías: {totalCalories}</p>
          </section>

          <section className="card">
            <ExerciseCatalog exercises={exercises} />
          </section>

          <section className="card">
            <h2>Resumen comparativo</h2>
            {longestExercise && (
              <p>
                Mayor duración: {longestExercise.name} (
                {longestExercise.duration} min)
              </p>
            )}
            {highestCalorieExercise && (
              <p>
                Más calorías : {highestCalorieExercise.name} (
                {calculateCalories(highestCalorieExercise)} cal,{" "}
                {calculateCaloriePercentage(
                  highestCalorieExercise,
                  totalCalories,
                )}
                % del total)
              </p>
            )}
            <h3>Contribución al total de calorías:</h3>
            {exercises.map((exercise) => (
              <p key={exercise.id}>
                {exercise.name} ( {calculateCalories(exercise)} cal,{" "}
                {calculateCaloriePercentage(exercise, totalCalories)}% del
                total)
              </p>
            ))}
          </section>
        </div>
        <div className="results-container">
          <div className="column-heading">
            <h2>Seguimiento de usuarios</h2>
            <p>Control individual de entrenamientos y progreso</p>
          </div>
          <section className="card">
            <h2>Seleccionar usuario:</h2>

            <select
              value={selectedUserId ?? ""}
              onChange={(event) => {
                setSelectedUserId(
                  event.target.value === "" ? null : Number(event.target.value),
                );
              }}
            >
              <option value="">Seleccione un usuario</option>

              {users.map((user) => (
                <option key={user.id} value={user.id}>
                  {user.name}
                </option>
              ))}
            </select>
            {!selectedUser && (
              <p>Seleccione un usuario para crear o asignar una rutina.</p>
            )}
          </section>
          {selectedUser && (
            <section className="card">
              <h2>Perfil de Usuario</h2>
              <p>Nombre: {selectedUser.name}</p>
              <p>Edad: {selectedUser.age}</p>
              <p>Nivel: {selectedUser.experienceLevel}</p>
              <p>Membresía: {selectedUser.membershipPlan}</p>
              <p>
                Fecha de inicio:{" "}
                {selectedUser.startDate.toLocaleDateString("es-CR")}
              </p>
              <p>
                Membresía activa:{" "}
                {selectedUser.isActive ? "Activa" : "Inactiva"}
              </p>
            </section>
          )}
          {selectedUser && (
            <>
              {selectedUser.routine && (
                <p>
                  Este usuario ya tiene una rutina asignada. Si creas una nueva,
                  reemplazará la anterior.
                </p>
              )}

              <RoutineForm
                key={selectedUser.id}
                exercises={exercises}
                onCreateRoutine={handleRoutineCreate}
              />
            </>
          )}

          {selectedUser?.routine && (
            <RoutineView
              routine={selectedUser.routine}
              onToggleExercise={handleToggleExercise}
            />
          )}
          {weeklyLoad && restRecommendation && (
            <WeeklyLoadView
              weeklyLoad={weeklyLoad}
              restRecommendation={restRecommendation}
            />
          )}
        </div>
      </div>
    </>
  );
}

export default App;
