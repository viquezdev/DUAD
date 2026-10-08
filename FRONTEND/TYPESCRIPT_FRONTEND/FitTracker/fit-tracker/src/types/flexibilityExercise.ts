import type { BaseExercise } from "./exercise.ts";

export interface FlexibilityExercise extends BaseExercise {
  category: "flexibility";
  poses: number;
}
