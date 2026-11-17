import type { BaseExercise } from "./exercise.ts";
import type { HeartRateZone } from "./heartRateZone.ts";

export interface CardioExercise extends BaseExercise {
  category: "cardio";
  distance: number;
  heartRateZone: HeartRateZone;
}
