import React from "react";
import { View, Text, FlatList, TouchableOpacity, Image } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { useRouter, useSearchParams } from "expo-router/build/hooks";

// Dados das atividades (poderiam vir de uma API ou ser dinâmicos)
const atividadesData = {
  "20": [
    // Atividades para a turma 4DSN
    {
      id: "1",
      nome: "DER",
      dataEntrega: "31/09",
      horario: "1 PM",
      entregas: 3,
    },
    // Outras atividades para 4DSN
  ],
  "21": [
    // Atividades para a turma 3DSN
    {
      id: "1",
      nome: "Matemática",
      dataEntrega: "01/10",
      horario: "3 PM",
      entregas: 2,
    },
    // Outras atividades para 3DSN
  ],
};

const Atividades = () => {
  const router = useRouter();
  const searchParams = useSearchParams();
  const id = searchParams.get("id") || ""; // Obtém o ID da turma a partir dos parâmetros da URL
  const atividades = atividadesData[id as keyof typeof atividadesData] || []; // Obtém as atividades baseadas no ID

  const renderAtividade = ({
    item,
  }: {
    item: {
      id: string;
      nome: string;
      dataEntrega: string;
      horario: string;
      entregas: number;
    };
  }) => (
    <View
      style={{
        flexDirection: "row",
        borderWidth: 1,
        borderColor: "#ccc",
        borderRadius: 10,
        padding: 10,
        marginBottom: 10,
        alignItems: "center",
      }}
    >
      <View
        style={{
          width: 50,
          height: 50,
          borderRadius: 25,
          backgroundColor: "#eee",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Text style={{ fontWeight: "bold" }}>{item.nome}</Text>
      </View>
      <View style={{ flex: 1, marginLeft: 10 }}>
        <Text>
          DATA DE ENTREGA: {item.dataEntrega} | {item.horario}
        </Text>
      </View>
      <View style={{ alignItems: "center" }}>
        <Text>{item.entregas}</Text>
        <Image style={{ width: 30, height: 30, borderRadius: 15 }} />
      </View>
    </View>
  );

  return (
    <View style={{ flex: 1, backgroundColor: "#fff", padding: 10 }}>
      {/* Cabeçalho */}
      <View
        style={{
          flexDirection: "row",
          alignItems: "center",
          paddingVertical: 10,
          borderBottomWidth: 1,
          borderColor: "#ccc",
        }}
      >
        <Image
          source={require("../../images/livro.png")}
          style={{ width: 40, height: 40, marginRight: 10 }}
        />
        <Text style={{ fontSize: 18, fontWeight: "bold" }}>
          MINERVA &gt; {id === "20" ? "4DSN" : "3DSN"}
        </Text>
      </View>

      {/* Lista de Atividades */}
      <FlatList
        data={atividades}
        keyExtractor={(item) => item.id}
        renderItem={renderAtividade}
      />

      {/* Rodapé */}
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

export default Atividades;
