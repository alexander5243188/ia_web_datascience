import { Image } from 'expo-image';
import { Platform } from 'react-native';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { View,Text, StyleSheet } from 'react-native';

export default function AboutScreen() {
  const nombre = "Rosa";
  const edad = 16;
  const isPremiun = true;
  const massages = 5;

  return (
   <View style={styles.container}>
    <Text>Colegiala {nombre}</Text>
    <Text>tetona ardiente. de edad {edad}</Text>
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
