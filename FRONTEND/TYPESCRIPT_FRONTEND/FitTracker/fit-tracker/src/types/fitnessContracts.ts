import type { WeeklyRoutine } from "./weeklyRoutine";
import type { WeeklyLoad } from "./weeklyLoad";
import type { RestRecommendation } from "./restRecommendation";
import type { DaySession } from "./daySession";
import type { RoutineExercise } from "./routineExercise";

export type CalculateWeeklyLoad = (weeklyRoutine: WeeklyRoutine) => WeeklyLoad;
export type GetRestRecommendation = (
  weeklyLoad: WeeklyLoad,
) => RestRecommendation;
export type FindHighestCalorieDay = (
  weeklyRoutine: WeeklyRoutine,
) => DaySession | null;
export type GetPendingExercises = (
  weeklyRoutine: WeeklyRoutine,
) => RoutineExercise[];
