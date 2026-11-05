import type { WeeklyRoutine } from "./weeklyRoutine";
import type { WeeklyLoad } from "./weeklyLoad";
import type { RestRecommendation } from "./restRecommendation";
import type { DaySession } from "./daySession";
import type { RoutineExercise } from "./routineExercise";
import type { WeeklySummary } from "./weeklySummary";
import type { Instructor } from "./instructor";

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
export type GetWeeklySummary = (
  name: string,
  weeklyRoutine: WeeklyRoutine,
) => WeeklySummary;
export type GetInstructorWeeklySummaries = (
  instructor: Instructor,
) => WeeklySummary[];
