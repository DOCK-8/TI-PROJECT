const images = import.meta.glob('../assets/*.webp', { eager: true, import: 'default' });

export const iconMap = {
  "Horno Eléctrico": images['../assets/HornoElectrico.webp'],
  "Hervidor de agua": images['../assets/Hervidor.webp'],
  "Microondas": images['../assets/Microondas.webp'],
  "Waflera": images['../assets/Waflera.webp'],
  "Olla arrocera": images['../assets/OllaArrocera.webp'],
  "Tostadora": images['../assets/Tostadora.webp'],
  "Cafetera": images['../assets/Cafetera.webp'],
  "Licuadora": images['../assets/Licuadora.webp'],
  "Refrigeradora": images['../assets/Refrigeradora.webp'],
  "Batidora": images['../assets/Batidora.webp'],
  "Campana extractora": images['../assets/CampanaExtractora.webp'],

  // Sala
  "Aire acondicionado": images['../assets/AireAcondicionado.webp'],
  "Foco LED": images['../assets/FocoLED.webp'],
  "Televisor": images['../assets/Televisor.webp'],
  "Equipo de sonido": images['../assets/EquipoSonido.webp'],
  "Laptop": images['../assets/Laptop.webp'],
  "DVD": images['../assets/DVD.webp'],

  // Dormitorio
  "Computadora": images['../assets/Computadora.webp'],
  "Ventilador": images['../assets/Ventilador.webp'],
  "Play Station": images['../assets/PlayStation.webp'],
  "Cargador de celular": images['../assets/CargadorCelular.webp'],

  // Baño
  "Ducha eléctrica": images['../assets/DuchaEléctrica.webp'],
  "Terma eléctrica": images['../assets/TermaElectrica.webp'],
  "Secadora de cabello": images['../assets/SecadoraCabello.webp'],

  // Lavandería
  "Secadora de ropa": images['../assets/SecadoraRopa.webp'],
  "Plancha": images['../assets/Plancha.webp'],
  "Aspiradora": images['../assets/Aspiradora.webp'],
  "Lustradora": images['../assets/Lustradora.webp'],
  "Lavadora": images['../assets/Lavadora.webp'],
};
