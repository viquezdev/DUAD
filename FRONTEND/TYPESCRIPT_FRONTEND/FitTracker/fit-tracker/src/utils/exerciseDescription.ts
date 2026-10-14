import type { Exercise } from "../types/exercise";
import {
  calculateCalories,
  formatDuration,
  calculatePace,
} from "../utils/fitness.ts";

export function describeExercise(exercise: Exercise): string {
  switch (exercise.category) {
    case "cardio": {
      const pace = calculatePace(exercise);
      return `${exercise.name}, ${formatDuration(exercise.duration)} | ${exercise.distance} km | zona cardíaca ${exercise.heartRateZone} | ${calculateCalories(exercise)} cal ${pace !== null ? ` - Pace: ${pace} min/km` : ""}  `;
    }
    case "strength": {
      return `${exercise.name}, ${formatDuration(exercise.duration)} | ${exercise.sets} series de ${exercise.reps} reps | ${exercise.weight} kg | ${calculateCalories(exercise)} cal   `;
    }
    case "flexibility": {
      return `${exercise.name}, ${formatDuration(exercise.duration)} | ${exercise.poses} poses | ${calculateCalories(exercise)} cal   `;
    }
  }
}
