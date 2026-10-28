import type { RestRecommendation } from "./restRecommendation";

export interface WeeklySummary {
  name: string;
  trainingDays: number;
  totalMinutes: number;
  totalCalories: number;
  restRecommendation: RestRecommendation;
  pendingExercises: number;
}
