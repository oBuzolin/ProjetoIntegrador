import React from "react";
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import semiDeusesStyles from "../../styles/semiDeusesStyle";
import { useRouter } from "expo-router";
import { useSearchParams } from "expo-router/build/hooks";

const SemiDeuses = () => {
  const router = useRouter();
  const searchParams = useSearchParams();
  const id = searchParams.get("id") || "";
  const styles = semiDeusesStyles;

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>
          {" "}
          MINERVA &gt; {id === "20" ? "4DSN" : "3DSN"}
        </Text>
      </View>
      <ScrollView style={styles.scrollView}>
        <Text style={styles.sectionTitle}>DEUSES</Text>
        <View style={styles.userRow}>
          <Ionicons name="person-circle-outline" size={24} color="black" />
          <Text style={styles.userText}>PROFESSOR</Text>
          <TouchableOpacity>
            <Ionicons name="mail-outline" size={24} color="black" />
          </TouchableOpacity>
        </View>
        <Text style={styles.sectionTitle}>SEMI-DEUSES</Text>
        {["ALUNO", "ALUNO", "ALUNO", "ALUNO", "ALUNO"].map((student, index) => (
          <View key={index} style={styles.userRow}>
            <Ionicons name="person-circle-outline" size={24} color="black" />
            <Text style={styles.userText}>{student}</Text>
            <TouchableOpacity>
              <Ionicons name="mail-outline" size={24} color="black" />
            </TouchableOpacity>
          </View>
        ))}
      </ScrollView>
      <View
        style={{
          flexDirection: "row",
          justifyContent: "space-around",
          paddingVertical: 10,
          borderTopWidth: 1,
          borderColor: "#ccc",
        }}
      >
        <TouchableOpacity
          style={{ alignItems: "center" }}
          onPress={() => router.push(`/${id}`)}
        >
          <Ionicons name="chatbubble-outline" size={30} color="teal" />
          <Text>Mural</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{ alignItems: "center" }}
          onPress={() => router.push(`/atividades/${id}`)}
        >
          <Ionicons name="clipboard-outline" size={30} color="teal" />
          <Text>Atividades</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{ alignItems: "center" }}
          onPress={() => router.push(`/semideuses/${id}`)}
        >
          <Ionicons name="person-circle-outline" size={30} color="teal" />
          <Text>Semi-deuses</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default SemiDeuses;
