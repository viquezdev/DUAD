import type { RestRecommendation } from "./restRecommendation";

export interface WeeklySummary {
  name: string;
  hasRoutine: boolean;
  trainingDays: number;
  totalMinutes: number;
  totalCalories: number;
  restRecommendation?: RestRecommendation;
  pendingExercises: number;
}
