import type { RestRecommendation } from "./restRecommendation";
import type { RoutineExercise } from "./routineExercise";

export interface WeeklySummary {
  name: string;
  hasRoutine: boolean;
  trainingDays: number;
  totalMinutes: number;
  totalCalories: number;
  restRecommendation?: RestRecommendation;
  pendingExercises: RoutineExercise[]; // Updated type to include RoutineExercise IDs
}
