import { useState } from "react";
import type { CaloriesPerMinute } from "../../types/caloriesPerMinute";
import type { Category } from "../../types/category";
import type { HeartRateZone } from "../../types/heartRateZone";
import type { NewExercise } from "../../types/exercise";
import "./ExerciseForm.css";

export const ExerciseForm = ({ onSubmit }: ExerciseFormProps) => {
  const [name, setName] = useState<string>("");
  const [duration, setDuration] = useState<number>(0);
  const [caloriesPerMinute, setCaloriesPerMinute] =
    useState<CaloriesPerMinute>(0);
  const [distance, setDistance] = useState<number>(0);
  const [category, setCategory] = useState<Category>("cardio");
  const [heartRateZone, setHeartRateZone] = useState<HeartRateZone>(1);
  const [sets, setSets] = useState<number>(0);
  const [reps, setReps] = useState<number>(0);
  const [weight, setWeight] = useState<number>(0);
  const [poses, setPoses] = useState<number>(0);

  return (
    <div className="exercise-form">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim() || duration <= 0 || caloriesPerMinute <= 0) {
            return;
          }

          if (category === "cardio") {
            if (distance <= 0) return;

            onSubmit({
              name,
              duration,
              caloriesPerMinute,
              category: "cardio",
              distance,
              heartRateZone,
            });
          } else if (category === "strength") {
            if (sets <= 0 || reps <= 0 || weight < 0) return;

            onSubmit({
              name,
              duration,
              caloriesPerMinute,
              category: "strength",
              sets,
              reps,
              weight,
            });
          } else {
            if (poses <= 0) return;

            onSubmit({
              name,
              duration,
              caloriesPerMinute,
              category: "flexibility",
              poses,
            });
          }
          setDistance(0);
          setName("");
          setDuration(0);
          setCaloriesPerMinute(0);
          setHeartRateZone(1);
          setSets(0);
          setReps(0);
          setWeight(0);
          setPoses(0);
        }}
      >
        <h2>Registro de ejercicio</h2>
        <label htmlFor="category">Categoría:</label>
        <select
          id="category"
          value={category}
          onChange={(e) => setCategory(e.target.value as Category)}
        >
          <option value="cardio">Cardio</option>
          <option value="strength">Fuerza</option>
          <option value="flexibility">Flexibilidad</option>
        </select>
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
        {category === "cardio" && (
          <>
            <label htmlFor="distance">Distancia (km):</label>
            <input
              type="number"
              id="distance"
              min="0.1"
              step="0.1"
              value={distance}
              onChange={(e) => setDistance(Number(e.target.value))}
            />

            <label htmlFor="heartRateZone">Zona cardíaca:</label>
            <select
              id="heartRateZone"
              value={heartRateZone}
              onChange={(e) =>
                setHeartRateZone(Number(e.target.value) as HeartRateZone)
              }
            >
              <option value={1}>Zona 1</option>
              <option value={2}>Zona 2</option>
              <option value={3}>Zona 3</option>
              <option value={4}>Zona 4</option>
              <option value={5}>Zona 5</option>
            </select>
          </>
        )}

        {category === "strength" && (
          <>
            <label htmlFor="sets">Series:</label>
            <input
              type="number"
              id="sets"
              min="1"
              value={sets}
              onChange={(e) => setSets(Number(e.target.value))}
            />

            <label htmlFor="reps">Repeticiones por serie:</label>
            <input
              type="number"
              id="reps"
              min="1"
              value={reps}
              onChange={(e) => setReps(Number(e.target.value))}
            />

            <label htmlFor="weight">Peso (kg):</label>
            <input
              type="number"
              id="weight"
              min="0"
              step="0.5"
              value={weight}
              onChange={(e) => setWeight(Number(e.target.value))}
            />
          </>
        )}

        {category === "flexibility" && (
          <>
            <label htmlFor="poses">Cantidad de posturas:</label>
            <input
              type="number"
              id="poses"
              min="1"
              value={poses}
              onChange={(e) => setPoses(Number(e.target.value))}
            />
          </>
        )}

        <button type="submit">Registrar ejercicio</button>
      </form>
    </div>
  );
};

type ExerciseFormProps = {
  onSubmit: (data: NewExercise) => void;
};

export default ExerciseForm;
