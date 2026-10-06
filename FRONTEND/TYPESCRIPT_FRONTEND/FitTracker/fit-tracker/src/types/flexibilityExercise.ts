import type { Exercise } from "./exercise.ts";

export interface FlexibilityExercise extends Exercise {
  category: "flexibility";
  poses: number;
}
