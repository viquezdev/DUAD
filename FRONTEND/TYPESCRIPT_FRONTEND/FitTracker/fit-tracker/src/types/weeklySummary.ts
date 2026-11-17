import type { RestRecommendation } from "./restRecommendation";
import type { RoutineExercise } from "./routineExercise";
import type { User } from "./user";

export interface WeeklySummary {
  name: string;
  hasRoutine: boolean;
  trainingDays: number;
  totalMinutes: number;
  totalCalories: number;
  restRecommendation?: RestRecommendation;
  pendingExercises: RoutineExercise[];
  userId: User["id"];
  experienceLevel: User["experienceLevel"];
  routineName: string | null;
}
