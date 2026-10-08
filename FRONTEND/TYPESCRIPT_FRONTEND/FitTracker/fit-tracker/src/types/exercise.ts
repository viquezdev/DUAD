import type { CaloriesPerMinute } from "./caloriesPerMinute";
import type { FlexibilityExercise } from "./flexibilityExercise";
import type { StrengthExercise } from "./strengthExercise";
import type { CardioExercise } from "./cardioExercise";

export interface BaseExercise {
  name: string;
  duration: number;
  caloriesPerMinute: CaloriesPerMinute;
}

export type Exercise = FlexibilityExercise | StrengthExercise | CardioExercise;
