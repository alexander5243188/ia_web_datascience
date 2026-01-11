import { Image } from 'expo-image';
import { Platform } from 'react-native';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { View,Text, StyleSheet } from 'react-native';
import {ejemploDestructuracionUsuario} from '@/utils/math'

export default function AboutScreen() {
  const nombre = "Mary Paz";
  const edad = 21;  
  const isPremiun = true;  
  const messages = 5;
  const fecha = new Date();
  const hora = fecha.getHours();
  let saludo =  hora < 12 ? "Buenos dias" : hora < 18 ? "Buenas tardes" : "Buenas noches";

  return (
   <View style={styles.container}>
    <Text>Hola {nombre}</Text>
    <Text>En 5 años tendras {edad + 5}</Text>
    <Text> {isPremiun ? "Plan pago" : "Plan gatruito"} </Text>
    {messages > 0 && <Text>Tienes {messages} mensajes nuevos</Text>}
    <Text>Tu edad es {edad}</Text>
    <Text>{saludo}</Text>
    <Text>{ejemploDestructuracionUsuario()}</Text>
   </View>
  );
}

const styles = StyleSheet.create({
  container:{
    flex:1,
    alignItems: "center",
    justifyContent:"center",
    backgroundColor:"#f2f6ff",
    padding: 23,
    gap: 8,
  },  
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
