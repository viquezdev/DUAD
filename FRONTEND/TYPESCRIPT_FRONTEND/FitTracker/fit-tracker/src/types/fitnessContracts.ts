import type { WeeklyRoutine } from "./weeklyRoutine";
import type { WeeklyLoad } from "./weeklyLoad";
import type { RestRecommendation } from "./restRecommendation";
import type { DaySession } from "./daySession";
import type { RoutineExercise } from "./routineExercise";
import type { WeeklySummary } from "./weeklySummary";
import type { Instructor } from "./instructor";
import type { User } from "./user";
import type { Exercise } from "./exercise";

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
export type GetWeeklySummary = (user: User) => WeeklySummary;
export type GetInstructorWeeklySummaries = (
  instructor: Instructor,
  users: User[],
) => WeeklySummary[];
export type CalculateCalories = (exercise: Exercise) => number;
export type CalculatePace = (exercise: Exercise) => number | null;
export type CalculateAverageCalories = (weeklyRoutine: WeeklyRoutine) => number;
export type FormatDuration = (duration: number) => string;
export type FindLongestExercise = (exercises: Exercise[]) => Exercise | null;
export type FindHighestCalorieExercise = (
  exercises: Exercise[],
) => Exercise | null;
export type CalculateCaloriePercentage = (
  exercise: Exercise,
  totalCalories: number,
) => number;
export type CalculateTotalMinutes = (weeklyRoutine: WeeklyRoutine) => number;
export type CalculateTotalCalories = (weeklyRoutine: WeeklyRoutine) => number;
export type CalculateTrainingDays = (weeklyRoutine: WeeklyRoutine) => number;
export type CalculateMinutesByCategory = (
  weeklyRoutine: WeeklyRoutine,
  category: Exercise["category"],
) => number;
