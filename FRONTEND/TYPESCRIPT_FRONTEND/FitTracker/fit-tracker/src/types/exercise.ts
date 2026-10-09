import type { CaloriesPerMinute } from "./caloriesPerMinute";
import type { FlexibilityExercise } from "./flexibilityExercise";
import type { StrengthExercise } from "./strengthExercise";
import type { CardioExercise } from "./cardioExercise";
import type { ExerciseId } from "./exerciseId";

export interface BaseExercise {
  id: ExerciseId;
  name: string;
  duration: number;
  caloriesPerMinute: CaloriesPerMinute;
}

export type Exercise = FlexibilityExercise | StrengthExercise | CardioExercise;
