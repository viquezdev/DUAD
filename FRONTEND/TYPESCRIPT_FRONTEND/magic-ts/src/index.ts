import {
  getCardsByName,
  getCardsByColor,
  getCardsByRarity,
  getCachedCard,
} from "./api";

async function main() {
  const cartas = await getCardsByColor("White"); // Cambia "Blue" por el color que desees buscar
  const cartasPorRareza = await getCardsByRarity("Rare"); // Cambia "Uncommon" por la rareza que desees buscar
  const cartaEnCache = await getCachedCard("Lightning Bolt"); // Cambia "Lightning Bolt" por el nombre de la carta que desees buscar en cache

  if (cartaEnCache) {
    console.log(`🎴 Nombre: ${cartaEnCache.name}`);
    console.log(`🪄 Tipo: ${cartaEnCache.type}`);
    console.log(`🌈 Colores: ${cartaEnCache.colors?.join(", ") ?? "Incoloro"}`);
    console.log(`🖌️ Rareza: ${cartaEnCache.rarity}`);
  } else {
    console.log("No se encontró la carta en cache.");
  }

  if (cartasPorRareza.length === 0) {
    console.log("No se encontraron cartas.");
    return;
  }

  cartasPorRareza.forEach((carta) => {
    console.log(`🎴 Nombre: ${carta.name}`);
    console.log(`🪄 Tipo: ${carta.type}`);
    console.log(`🌈 Colores: ${carta.colors?.join(", ") ?? "Incoloro"}`);
    console.log(`🖌️ Rareza: ${carta.rarity}`);
    console.log("=====================================");
  });
}

main();
