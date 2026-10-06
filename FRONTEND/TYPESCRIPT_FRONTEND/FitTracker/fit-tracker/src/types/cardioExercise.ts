import type { Exercise } from "./exercise.ts";
import type { HeartRateZone } from "./heartRateZone.ts";

export interface CardioExercise extends Exercise {
  category: "cardio";
  distance: number;
  heartRateZone: HeartRateZone;
}
