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
  const [profile, setProfile] = useState<UserFormData | null>(null);
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [routine, setRoutine] = useState<WeeklyRoutine | null>(null);
  const handleUserSubmit = (data: UserFormData) => {
    setProfile(data);
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
    setRoutine(newRoutine);
  };
  const handleToggleExercise = (
    day: DayOfWeek,
    exerciseId: RoutineExercise["id"],
  ) => {
    setRoutine((currentRoutine) => {
      if (!currentRoutine) {
        return currentRoutine;
      }

      return {
        ...currentRoutine,
        sessions: currentRoutine.sessions.map((session) => {
          if (session.day !== day) {
            return session;
          }

          return {
            ...session,
            exercises: session.exercises.map((exercise) => {
              if (exercise.id === exerciseId) {
                return {
                  ...exercise,
                  isCompleted: !exercise.isCompleted,
                };
              }
              return exercise;
            }),
          };
        }),
      };
    });
  };
  const user: User | null =
    profile && routine
      ? {
          id: 1,
          name: profile.name,
          age: profile.age,
          email: profile.email,
          experienceLevel: profile.experienceLevel,
          membershipPlan: profile.membershipPlan,
          startDate: profile.startDate,
          isActive: profile.isActive,
          routine,
        }
      : null;
  const longestExercise = findLongestExercise(exercises);
  const highestCalorieExercise = findHighestCalorieExercise(exercises);
  const totalCalories = exercises.reduce(
    (total, exercise) => total + calculateCalories(exercise),
    0,
  );
  const weeklyLoad = routine ? calculateWeeklyLoad(routine) : null;
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
          <UserForm onSubmit={handleUserSubmit} />

          <ExerciseForm onSubmit={handleExerciseSubmit} />
          <RoutineForm
            exercises={exercises}
            onCreateRoutine={handleRoutineCreate}
          />
        </div>
        <div className="results-container">
          {profile && (
            <section className="card">
              <h2>Perfil de Usuario</h2>
              <p>Nombre: {profile.name}</p>
              <p>Edad: {profile.age}</p>
              <p>Nivel: {profile.experienceLevel}</p>
              <p>Membresía: {profile.membershipPlan}</p>
              <p>
                Fecha de inicio: {profile.startDate.toLocaleDateString("es-CR")}
              </p>
              <p>
                Membresía activa: {profile.isActive ? "Activa" : "Inactiva"}
              </p>
            </section>
          )}

          {routine && (
            <div>
              <RoutineView
                routine={routine}
                onToggleExercise={handleToggleExercise}
              />
            </div>
          )}
          {weeklyLoad && restRecommendation && (
            <WeeklyLoadView
              weeklyLoad={weeklyLoad}
              restRecommendation={restRecommendation}
            />
          )}
          <section className="card">
            <h2>Ejercicios registrados</h2>
            {exercises.map((exercise, index) => {
              const pace = calculatePace(exercise);
              return (
                <p key={index}>
                  {exercise.name} - {formatDuration(exercise.duration)} -{" "}
                  {calculateCalories(exercise)} cal
                  {pace !== null ? ` - Pace: ${pace} min/km` : ""}
                </p>
              );
            })}
            <p>Total de calorías: {totalCalories}</p>
          </section>
          {profile && (
            <section className="card">
              <ExerciseCatalog exercises={exercises} profile={profile} />
            </section>
          )}
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
      </div>
    </>
  );
}

export default App;
