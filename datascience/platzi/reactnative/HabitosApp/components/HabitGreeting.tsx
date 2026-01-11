import { View, Text, StyleSheet } from "react-native";

export default function HabitGreeting({nombre = "Mary paz"}) {
    const fecha = new Date();
    const h = fecha.getHours();
    const saludo = h < 12 ? "Buenos dias" : h<18 ? "Buenas tardes" : "Buenas noches"
    return(
        <View style={styles.container} >
            <Text style={styles.title}>
                {saludo}
                {nombre ? `, ${nombre}`: ""}
            </Text>
            <Text style={styles.subtitle}>
                Hoy es {fecha.toLocaleDateString()} - {fecha.toLocaleDateString()} 
            </Text>
        </View>
    )
    const styles = StyleSheet.create({
        container:{gap: 4, marginBottom:16 },
        title:{fontSize: 22, fontWeight: "700"},
        subtitle:{fontSize: 12, color:"#475569"}
    });
}