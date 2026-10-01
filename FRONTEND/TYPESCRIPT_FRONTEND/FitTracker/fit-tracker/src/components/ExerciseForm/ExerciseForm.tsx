import { useState } from "react";
import type { CaloriesPerMinute } from "../../types/caloriesPerMinute";
import type { Exercise } from "../../types/exercise";
import "./ExerciseForm.css";

export const ExerciseForm = ({ onSubmit }: ExerciseFormProps) => {
  const [name, setName] = useState<string>("");
  const [duration, setDuration] = useState<number>(0);
  const [caloriesPerMinute, setCaloriesPerMinute] =
    useState<CaloriesPerMinute>(0);
  const [distance, setDistance] = useState<number>(0);
  return (
    <div className="exercise-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (distance === 0) {
            onSubmit({ name, duration, caloriesPerMinute });
          } else {
            onSubmit({ name, duration, caloriesPerMinute, distance });
          }
          setDistance(0);
          setName("");
          setDuration(0);
          setCaloriesPerMinute(0);
        }}
      >
        <h2>Registro de ejercicio</h2>
        <label htmlFor="exercise-name">Nombre:</label>
        <input
          type="text"
          id="exercise-name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <label htmlFor="duration">Duración:</label>
        <input
          type="number"
          id="duration"
          value={duration}
          onChange={(e) => setDuration(Number(e.target.value))}
        />
        <label htmlFor="caloriesPerMinute">Calorías por minuto:</label>
        <input
          type="number"
          id="caloriesPerMinute"
          value={caloriesPerMinute}
          onChange={(e) =>
            setCaloriesPerMinute(Number(e.target.value) as CaloriesPerMinute)
          }
        />

        <label htmlFor="distance">Distancia:</label>
        <input
          type="number"
          id="distance"
          value={distance}
          onChange={(e) => setDistance(Number(e.target.value))}
        />

        <button type="submit">Registrar ejercicio</button>
      </form>
    </div>
  );
};

type ExerciseFormProps = {
  onSubmit: (data: Exercise) => void;
};

export default ExerciseForm;
