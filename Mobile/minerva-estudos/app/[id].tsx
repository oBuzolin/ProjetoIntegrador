import React from "react";
import {
  View,
  TextInput,
  FlatList,
  TouchableOpacity,
  Image,
  Dimensions,
  Text,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import RenderHTML from "react-native-render-html";
import turmaStyles from "../styles/turmaStyle";
import { useRouter, useSearchParams } from "expo-router/build/hooks";

const DetalhesTurma = () => {
  const styles = turmaStyles;
  const router = useRouter();
  const searchParams = useSearchParams();
  const id = searchParams.get("id");
  const nomeTurma = id === "20" ? "4DSN" : "3DSN"; // Exemplo para vincular id com nome (substituir por dados reais)

  const mensagens = [
    { id: "1", html: "<p><strong>Professor:</strong> Bem-vindo à turma!</p>" },
    {
      id: "2",
      html: "<p><strong>Professor:</strong></em> Não se esqueçam da atividade de amanhã!</p>",
    },
  ];

  const renderMensagem = ({ item }: { item: { id: string; html: string } }) => (
    <View style={styles.mensagemContainer}>
      <RenderHTML
        contentWidth={Dimensions.get("window").width - 40} // Define a largura máxima para o HTML
        source={{ html: item.html }}
      />
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Cabeçalho */}
      <View style={styles.header}>
        <Image source={require("../images/livro.png")} style={styles.logo} />
        <Text style={styles.headerText}>MINERVA &gt; {nomeTurma}</Text>
      </View>

      {/* Card da turma */}
      <View style={styles.cardTurma}>
        <View style={styles.cardInfo}>
          <Text style={styles.cardNome}>{nomeTurma}</Text>
          <Ionicons name="person-circle-outline" size={40} color="black" />
        </View>
      </View>

      {/* Mural */}
      <TextInput
        style={styles.input}
        placeholder="Digite uma mensagem...!"
        placeholderTextColor="#999"
      />
      <FlatList
        data={mensagens}
        keyExtractor={(item) => item.id}
        renderItem={renderMensagem}
        style={styles.mural}
      />

      {/* Footer */}
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

export default DetalhesTurma;
