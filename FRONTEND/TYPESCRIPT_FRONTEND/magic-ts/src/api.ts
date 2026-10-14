import fetch from "node-fetch";
import { BaseApiResponse } from "./types";
import { MagicCard, ApiResponse, MagicColor, Rarity } from "./types";

// Función genérica para consumir la API
export async function fetchFromApi<T extends BaseApiResponse>(
  endpoint: string,
): Promise<T> {
  const url = `https://api.magicthegathering.io/v1/${endpoint}`;

  try {
    const response = await fetch(url);
    if (!response.ok)
      throw new Error(`Error en la API: ${response.statusText}`);

    // Validación de tipo en tiempo de ejecución
    const data = await response.json();
    if (!data || typeof data !== "object") {
      throw new Error("Respuesta inválida de la API");
    }

    return data as T; // Cast más seguro después de validación
  } catch (error) {
    console.error("Error en la petición:", error);
    throw error;
  }
}

// Función mejorada para buscar cartas por nombre con manejo de errores
export async function getCardsByName(name: string): Promise<MagicCard[]> {
  try {
    const data = await fetchFromApi<ApiResponse<MagicCard>>(
      `cards?name=${encodeURIComponent(name)}`,
    );
    return data.cards;
  } catch (error) {
    console.warn(`⚠️ Error al buscar cartas con nombre: ${name}`);
    console.error(error);
    return []; // Retornamos un array vacío en caso de error
  }
}

// Intenta implementar esta función
export async function getCardsByColor(color: MagicColor): Promise<MagicCard[]> {
  try {
    const data = await fetchFromApi<ApiResponse<MagicCard>>(
      `cards?colors=${encodeURIComponent(color)}`,
    );
    return data.cards;
  } catch (error) {
    console.warn(`⚠️ Error al buscar cartas con color: ${color}`);
    console.error(error);
    return []; // Retornamos un array vacío en caso de error
  }
}

// Ejercicio: Implementa esta función
export async function getCardsByRarity(rarity: Rarity): Promise<MagicCard[]> {
  try {
    const data = await fetchFromApi<ApiResponse<MagicCard>>(
      `cards?rarity=${encodeURIComponent(rarity)}`,
    );
    return data.cards;
  } catch (error) {
    console.warn(`⚠️ Error al buscar cartas con rareza: ${rarity}`);
    console.error(error);
    return []; // Retornamos un array vacío en caso de error
  }
}

// Ejercicio avanzado: Implementa un sistema de cache
const cardCache = new Map<string, MagicCard>();

// Implementa esta función usando el cache
export async function getCachedCard(name: string): Promise<MagicCard | null> {
  // Tip: Revisa el cache antes de llamar a la API
  if (cardCache.has(name)) {
    return cardCache.get(name) || null;
  }

  try {
    const card = await getCardsByName(name);
    if (card.length > 0) {
      cardCache.set(name, card[0]);
      return card[0];
    }
    return null;
  } catch (error) {
    console.error(`Error al buscar carta en cache: ${name}`, error);
    return null;
  }
}
