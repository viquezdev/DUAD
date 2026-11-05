import type { BaseExercise } from "./exercise.ts";

export interface StrengthExercise extends BaseExercise {
  category: "strength";
  sets: number;
  reps: number;
  weight: number;
}
