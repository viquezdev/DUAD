import type { Exercise } from "./exercise";

export type DayOfWeek =
  | "Lunes"
  | "Martes"
  | "Miércoles"
  | "Jueves"
  | "Viernes"
  | "Sábado"
  | "Domingo";

export interface RoutineEntry {
  day: DayOfWeek;
  exercise: Exercise;
}
