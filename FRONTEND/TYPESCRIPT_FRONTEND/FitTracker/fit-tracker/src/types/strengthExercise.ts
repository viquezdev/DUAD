import type { Exercise } from "./exercise.ts";

export interface StrengthExercise extends Exercise {
  category: "strength";
  sets: number;
  reps: number;
  weight: number;
}
