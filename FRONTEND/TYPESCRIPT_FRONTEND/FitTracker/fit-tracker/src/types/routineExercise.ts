import type { CardioExercise } from "./cardioExercise";
import type { StrengthExercise } from "./strengthExercise";
import type { FlexibilityExercise } from "./flexibilityExercise";

export interface CardioRoutineExercise extends CardioExercise {
  isCompleted: boolean;
  caloriesBurned: number;
}

export interface StrengthRoutineExercise extends StrengthExercise {
  isCompleted: boolean;
}

export interface FlexibilityRoutineExercise extends FlexibilityExercise {
  isCompleted: boolean;
  comment?: string;
}

export type RoutineExercise =
  | CardioRoutineExercise
  | StrengthRoutineExercise
  | FlexibilityRoutineExercise;
