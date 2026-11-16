import type { Exercise } from "../types/exercise";
import type { WeeklyRoutine } from "../types/weeklyRoutine";
import type { WeeklyLoad } from "../types/weeklyLoad";
import type { FindHighestCalorieDay } from "../types/fitnessContracts";
import type { DaySession } from "../types/daySession";
import type { GetPendingExercises } from "../types/fitnessContracts";
import type { CalculateWeeklyLoad } from "../types/fitnessContracts";
import type { GetRestRecommendation } from "../types/fitnessContracts";
import type { GetWeeklySummary } from "../types/fitnessContracts";
import type { GetInstructorWeeklySummaries } from "../types/fitnessContracts";
import type { Instructor } from "../types/instructor";
import type { User } from "../types/user";
import type { CalculateCalories } from "../types/fitnessContracts";
import type { CalculatePace } from "../types/fitnessContracts";
import type { CalculateAverageCalories } from "../types/fitnessContracts";
import type { FormatDuration } from "../types/fitnessContracts";
import type { FindLongestExercise } from "../types/fitnessContracts";
import type { FindHighestCalorieExercise } from "../types/fitnessContracts";
import type { CalculateCaloriePercentage } from "../types/fitnessContracts";
import type { CalculateTotalMinutes } from "../types/fitnessContracts";
import type { CalculateTotalCalories } from "../types/fitnessContracts";
import type { CalculateTrainingDays } from "../types/fitnessContracts";
import type { CalculateMinutesByCategory } from "../types/fitnessContracts";

export const calculateCalories: CalculateCalories = (exercise: Exercise) => {
  return exercise.duration * exercise.caloriesPerMinute;
};

export const calculatePace: CalculatePace = (exercise: Exercise) => {
  if (exercise.category === "cardio") {
    if (exercise.distance > 0 && exercise.duration > 0) {
      return Math.round((exercise.duration / exercise.distance) * 100) / 100;
    }
  }
  return null;
};

export const calculateAverageCalories: CalculateAverageCalories = (
  routine: WeeklyRoutine,
) => {
  const totalCalories = calculateTotalCalories(routine);
  const trainingDays = calculateTrainingDays(routine);
  return trainingDays > 0
    ? Math.round((totalCalories / trainingDays) * 100) / 100
    : 0;
};

export const formatDuration: FormatDuration = (duration: number) => {
  const hours = Math.floor(duration / 60);
  const minutes = duration % 60;
  if (hours === 0 && minutes === 0) {
    return "0min";
  }
  if (hours > 0 && minutes === 0) {
    return `${hours}h`;
  }
  if (hours > 0 && minutes > 0) {
    return `${hours}h ${minutes}min`;
  }
  return `${minutes}min`;
};

export const findLongestExercise: FindLongestExercise = (
  exercises: Exercise[],
) => {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((longest, current) => {
    return current.duration > longest.duration ? current : longest;
  });
};

export const findHighestCalorieExercise: FindHighestCalorieExercise = (
  exercises: Exercise[],
) => {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((highest, current) => {
    return calculateCalories(current) > calculateCalories(highest)
      ? current
      : highest;
  });
};

export const calculateCaloriePercentage: CalculateCaloriePercentage = (
  exercise: Exercise,
  totalCalories: number,
) => {
  if (totalCalories === 0) {
    return 0;
  }
  const exerciseCalories = calculateCalories(exercise);
  return Math.round((exerciseCalories / totalCalories) * 100);
};

export const calculateTotalMinutes: CalculateTotalMinutes = (
  weeklyRoutine: WeeklyRoutine,
) => {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalMinutes = exercises.reduce((total, ex) => total + ex.duration, 0);
  return totalMinutes;
};

export const calculateTotalCalories: CalculateTotalCalories = (
  weeklyRoutine: WeeklyRoutine,
) => {
  return weeklyRoutine.sessions.reduce((total, session) => {
    return total + calculateSessionCalories(session);
  }, 0);
};

export const calculateTrainingDays: CalculateTrainingDays = (
  weeklyRoutine: WeeklyRoutine,
) => {
  const sessions = weeklyRoutine.sessions.filter(
    (session) => session.exercises.length > 0,
  );
  return sessions.length;
};

export const calculateWeeklyLoad: CalculateWeeklyLoad = (
  weeklyRoutine: WeeklyRoutine,
) => {
  return {
    totalMinutes: calculateTotalMinutes(weeklyRoutine),
    totalCalories: calculateTotalCalories(weeklyRoutine),
    cardioMinutes: calculateMinutesByCategory(weeklyRoutine, "cardio"),
    strengthMinutes: calculateMinutesByCategory(weeklyRoutine, "strength"),
    flexibilityMinutes: calculateMinutesByCategory(
      weeklyRoutine,
      "flexibility",
    ),
    trainingDays: calculateTrainingDays(weeklyRoutine),
  };
};

export const getRestRecommendation: GetRestRecommendation = (
  weeklyLoad: WeeklyLoad,
) => {
  if (weeklyLoad.totalMinutes > 300 || weeklyLoad.trainingDays > 5) {
    return "high";
  }
  if (weeklyLoad.totalMinutes < 150 || weeklyLoad.trainingDays < 3) {
    return "low";
  }
  return "balanced";
};

function calculateSessionCalories(session: DaySession): number {
  return session.exercises.reduce((total, ex) => {
    switch (ex.category) {
      case "cardio":
        return total + ex.caloriesBurned;
      case "strength":
      case "flexibility":
        return total + calculateCalories(ex);
    }
  }, 0);
}

export const findHighestCalorieDay: FindHighestCalorieDay = (
  weeklyRoutine: WeeklyRoutine,
) => {
  if (weeklyRoutine.sessions.length === 0) {
    return null;
  }
  const highestCalorieDay = weeklyRoutine.sessions.reduce(
    (highest, current) => {
      const highestCalories = calculateSessionCalories(highest);
      const currentCalories = calculateSessionCalories(current);

      return currentCalories > highestCalories ? current : highest;
    },
    weeklyRoutine.sessions[0],
  );

  return highestCalorieDay;
};

export const getPendingExercises: GetPendingExercises = (
  weeklyRoutine: WeeklyRoutine,
) => {
  const weeklyExercises = weeklyRoutine.sessions.flatMap(
    (session) => session.exercises,
  );
  const pendingExercises = weeklyExercises.filter(
    (exercise) => !exercise.isCompleted,
  );
  return pendingExercises;
};

export const getWeeklySummary: GetWeeklySummary = (user: User) => {
  const weeklyRoutine = user.routine;
  if (!weeklyRoutine) {
    return {
      name: user.name,
      hasRoutine: false,
      trainingDays: 0,
      totalMinutes: 0,
      totalCalories: 0,
      pendingExercises: [],
      userId: user.id,
      experienceLevel: user.experienceLevel,
      routineName: null,
    };
  }

  return {
    name: user.name,
    hasRoutine: true,
    trainingDays: calculateTrainingDays(weeklyRoutine),
    totalMinutes: calculateTotalMinutes(weeklyRoutine),
    totalCalories: calculateTotalCalories(weeklyRoutine),
    restRecommendation: getRestRecommendation(
      calculateWeeklyLoad(weeklyRoutine),
    ),
    pendingExercises: getPendingExercises(weeklyRoutine),
    userId: user.id,
    experienceLevel: user.experienceLevel,
    routineName: weeklyRoutine.name,
  };
};

export const getInstructorWeeklySummaries: GetInstructorWeeklySummaries = (
  instructor: Instructor,
  users: User[],
) => {
  return instructor.assignedUsers
    .map((userId) => users.find((user) => user.id === userId))
    .filter((user) => user !== undefined)
    .map((user) => getWeeklySummary(user));
};

export const calculateMinutesByCategory: CalculateMinutesByCategory = (
  weeklyRoutine,
  category,
) => {
  const exercises = weeklyRoutine.sessions.flatMap(
    (session) => session.exercises,
  );

  return exercises.reduce((total, exercise) => {
    if (exercise.category === category) {
      return total + exercise.duration;
    }

    return total;
  }, 0);
};
