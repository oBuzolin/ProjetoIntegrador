import React from "react";
import { View, Text, FlatList, TouchableOpacity, Image } from "react-native";
import professorStyles from "@/styles/professorStyle";
import { Ionicons } from "@expo/vector-icons";
import { useRouter } from "expo-router";

const styles = professorStyles;

const ProfessorHome = () => {
  const router = useRouter();

  const turmas = [
    { id: "20", nome: "4DSN", icone: "user" },
    { id: "21", nome: "3DSN", icone: "user" },
  ];

  const renderItem = ({
    item,
  }: {
    item: { id: string; nome: string; icone: string };
  }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() => router.push(`/${item.id}`)}
    >
      <Text style={styles.turmaText}>{item.nome}</Text>
      <View style={styles.iconsContainer}>
        <Image
          //   source={require("./assets/column-icon.png")}
          style={styles.icon}
        />
        <Ionicons name="person-circle-outline" size={35} color={"black"} />
        <Image style={styles.icon} />
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Image source={require("../images/livro.png")} style={styles.logo} />
        <Text style={styles.title}>MINERVA ESTUDOS</Text>
      </View>
      <FlatList
        data={turmas}
        keyExtractor={(item) => item.id}
        renderItem={renderItem}
      />
      <View style={styles.footer}>
        <TouchableOpacity style={styles.footerButton}>
          <Ionicons name="book-outline" size={30} color={"teal"} />
          <Text style={styles.footerText}>Matérias</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.footerButton}>
          <Ionicons name="calendar-outline" size={30} color="teal" />
          <Text style={styles.footerText}>Pendentes</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.footerButton}>
          <Ionicons name="person-circle-outline" size={30} color="teal" />
          <Text style={styles.footerText}>Perfil</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default ProfessorHome;
