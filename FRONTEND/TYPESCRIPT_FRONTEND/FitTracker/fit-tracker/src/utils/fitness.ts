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

export function calculateCalories(exercise: Exercise): number {
  return exercise.duration * exercise.caloriesPerMinute;
}

export function calculatePace(exercise: Exercise): number | null {
  if (exercise.category === "cardio") {
    if (exercise.distance > 0 && exercise.duration > 0) {
      return Math.round((exercise.duration / exercise.distance) * 100) / 100;
    }
  }
  return null;
}

export function calculateAverageCalories(routine: WeeklyRoutine): number {
  const totalCalories = calculateTotalCalories(routine);
  const trainingDays = calculateTrainingDays(routine);
  return trainingDays > 0
    ? Math.round((totalCalories / trainingDays) * 100) / 100
    : 0;
}

export function formatDuration(duration: number): string {
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
}

export function findLongestExercise(exercises: Exercise[]): Exercise | null {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((longest, current) => {
    return current.duration > longest.duration ? current : longest;
  });
}

export function findHighestCalorieExercise(
  exercises: Exercise[],
): Exercise | null {
  if (exercises.length === 0) {
    return null;
  }
  return exercises.reduce((highest, current) => {
    return calculateCalories(current) > calculateCalories(highest)
      ? current
      : highest;
  });
}

export function calculateCaloriePercentage(
  exercise: Exercise,
  totalCalories: number,
): number {
  if (totalCalories === 0) {
    return 0;
  }
  const exerciseCalories = calculateCalories(exercise);
  return Math.round((exerciseCalories / totalCalories) * 100);
}

export function calculateTotalMinutes(weeklyRoutine: WeeklyRoutine): number {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalMinutes = exercises.reduce((total, ex) => total + ex.duration, 0);
  return totalMinutes;
}

export function calculateTotalCalories(weeklyRoutine: WeeklyRoutine): number {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalCalories = exercises.reduce((total, ex) => {
    switch (ex.category) {
      case "cardio":
        return total + ex.caloriesBurned;
      case "strength":
        return total + calculateCalories(ex);
      case "flexibility":
        return total + calculateCalories(ex);
    }
  }, 0);
  return totalCalories;
}

export function calculateCardioMinutes(weeklyRoutine: WeeklyRoutine): number {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalMinutes = exercises.reduce((total, ex) => {
    if (ex.category === "cardio") {
      return total + ex.duration;
    } else {
      return total;
    }
  }, 0);
  return totalMinutes;
}

export function calculateStrengthMinutes(weeklyRoutine: WeeklyRoutine): number {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalMinutes = exercises.reduce((total, ex) => {
    if (ex.category === "strength") {
      return total + ex.duration;
    } else {
      return total;
    }
  }, 0);
  return totalMinutes;
}

export function calculateFlexibilityMinutes(
  weeklyRoutine: WeeklyRoutine,
): number {
  const exercises = weeklyRoutine.sessions.flatMap((day) => day.exercises);
  const totalMinutes = exercises.reduce((total, ex) => {
    if (ex.category === "flexibility") {
      return total + ex.duration;
    } else {
      return total;
    }
  }, 0);
  return totalMinutes;
}

export function calculateTrainingDays(weeklyRoutine: WeeklyRoutine): number {
  const sessions = weeklyRoutine.sessions.filter(
    (session) => session.exercises.length > 0,
  );
  return sessions.length;
}

export const calculateWeeklyLoad: CalculateWeeklyLoad = (
  weeklyRoutine: WeeklyRoutine,
) => {
  return {
    totalMinutes: calculateTotalMinutes(weeklyRoutine),
    totalCalories: calculateTotalCalories(weeklyRoutine),
    cardioMinutes: calculateCardioMinutes(weeklyRoutine),
    strengthMinutes: calculateStrengthMinutes(weeklyRoutine),
    flexibilityMinutes: calculateFlexibilityMinutes(weeklyRoutine),
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

export const getWeeklySummary: GetWeeklySummary = (
  name: string,
  weeklyRoutine?: WeeklyRoutine,
) => {
  if (!weeklyRoutine) {
    return {
      name,
      hasRoutine: false,
      trainingDays: 0,
      totalMinutes: 0,
      totalCalories: 0,
      pendingExercises: 0,
    };
  }

  return {
    name,
    hasRoutine: true,
    trainingDays: calculateTrainingDays(weeklyRoutine),
    totalMinutes: calculateTotalMinutes(weeklyRoutine),
    totalCalories: calculateTotalCalories(weeklyRoutine),
    restRecommendation: getRestRecommendation(
      calculateWeeklyLoad(weeklyRoutine),
    ),
    pendingExercises: getPendingExercises(weeklyRoutine).length,
  };
};

export const getInstructorWeeklySummaries: GetInstructorWeeklySummaries = (
  instructor: Instructor,
  users: User[],
) => {
  return instructor.assignedUsers
    .map((userId) => users.find((user) => user.id === userId))
    .filter((user) => user !== undefined)
    .map((user) => getWeeklySummary(user.name, user.routine));
};
