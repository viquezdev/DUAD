import type { Exercise } from "../types/exercise";
import type { Category } from "../types/category";
import type { CategorySummary } from "../types/categorySummary";
import { calculateCalories } from "./fitness";

export function getExercisesByCategory(
  exercises: Exercise[],
  category: Category,
): Exercise[] {
  return exercises.filter((exercise) => exercise.category === category);
}

export function getCategorySummary(
  exercises: Exercise[],
  category: Category,
): CategorySummary {
  const exercisesByCategory = getExercisesByCategory(exercises, category);

  const totalMinutes = exercisesByCategory.reduce((total, entry) => {
    return total + entry.duration;
  }, 0);
  const totalCalories = exercisesByCategory.reduce((total, entry) => {
    return total + calculateCalories(entry);
  }, 0);

  return {
    category,
    exercises: exercisesByCategory,
    totalMinutes,
    totalCalories,
  };
}

export function getExerciseCatalog(exercises: Exercise[]): CategorySummary[] {
  const categories: Category[] = ["cardio", "strength", "flexibility"];

  return categories.map((category) => getCategorySummary(exercises, category));
}
