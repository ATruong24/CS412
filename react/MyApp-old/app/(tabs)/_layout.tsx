import React from 'react';
import { Text } from 'react-native';
import { Tabs } from 'expo-router';

function TabIcon({ emoji }: { emoji: string }) {
  return <Text style={{ fontSize: 22 }}>{emoji}</Text>;
}

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ tabBarActiveTintColor: '#2f6fed' }}>
      <Tabs.Screen
        name="index"
        options={{ title: 'Home', tabBarIcon: () => <TabIcon emoji="🏠" /> }}
      />
      <Tabs.Screen
        name="detail"
        options={{ title: 'Detail', tabBarIcon: () => <TabIcon emoji="📖" /> }}
      />
      <Tabs.Screen
        name="about"
        options={{ title: 'About', tabBarIcon: () => <TabIcon emoji="ℹ️" /> }}
      />
    </Tabs>
  );
}