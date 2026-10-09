import type { Exercise } from "../types/exercise";
import type { WeeklyRoutine } from "../types/weeklyRoutine";

export function calculateCalories(exercise: Exercise): number {
  return exercise.duration * exercise.caloriesPerMinute;
}

export function calculateRoutineCalories(routine: WeeklyRoutine): number {
  return routine.entries.reduce((total, entry) => {
    return total + calculateCalories(entry.exercise);
  }, 0);
}

export function calculatePace(exercise: Exercise): number | null {
  if (exercise.distance && exercise.duration > 0) {
    return Math.round((exercise.duration / exercise.distance) * 100) / 100;
  }
  return null;
}

export function getTrainingDays(routine: WeeklyRoutine): number {
  const days = new Set(routine.entries.map((entry) => entry.day));
  return days.size;
}

export function calculateAverageCalories(routine: WeeklyRoutine): number {
  const totalCalories = calculateRoutineCalories(routine);
  const trainingDays = getTrainingDays(routine);
  return trainingDays > 0
    ? Math.round((totalCalories / trainingDays) * 100) / 100
    : 0;
}

export function formatDuration(duration: number): string {
  const hours = Math.floor(duration / 60);
  const minutes = duration % 60;
  if (hours === 0 && minutes === 0) {
    return "0min";
  }
  if (hours > 0 && minutes === 0) {
    return `${hours}h`;
  }
  if (hours > 0 && minutes > 0) {
    return `${hours}h ${minutes}min`;
  }
  return `${minutes}min`;
}

export function findLongestExercise(exercises: Exercise[]): Exercise | null {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((longest, current) => {
    return current.duration > longest.duration ? current : longest;
  });
}

export function findHighestCalorieExercise(
  exercises: Exercise[],
): Exercise | null {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((highest, current) => {
    return calculateCalories(current) > calculateCalories(highest)
      ? current
      : highest;
  });
}

export function calculateCaloriePercentage(
  exercise: Exercise,
  totalCalories: number,
): number {
  if (totalCalories === 0) {
    return 0;
  }
  const exerciseCalories = calculateCalories(exercise);
  return Math.round((exerciseCalories / totalCalories) * 100);
}

export function findHighestCalorieDay(routine: WeeklyRoutine): string | null {
  if (routine.entries.length === 0) {
    return null;
  }
  const caloriesByDay = new Map<string, number>();
  for (const entry of routine.entries) {
    const calories = calculateCalories(entry.exercise);
    if (caloriesByDay.has(entry.day)) {
      const currentCalories = caloriesByDay.get(entry.day) ?? 0;
      caloriesByDay.set(entry.day, currentCalories + calories);
    } else {
      caloriesByDay.set(entry.day, calories);
    }
  }
  let highestCalorieDay = "";
  let highestCalories = 0;
  for (const [day, calories] of caloriesByDay) {
    if (calories > highestCalories) {
      highestCalories = calories;
      highestCalorieDay = day;
    }
  }

  return highestCalorieDay || null;
}
