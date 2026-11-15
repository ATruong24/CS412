import { ScrollView, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

// Replace USERNAME and the file names with your own uploads on cs-people.
const BASE = 'https://cs-people.bu.edu/USERNAME/images';

export default function DetailScreen() {
  return (
    <ScrollView contentContainerStyle={styles.scrollContainer}>
      <Text style={styles.titleText}>TODO: Detail Title</Text>

      <Text style={styles.bodyText}>TODO: Intro paragraph about your interest.</Text>

      {/* Remote images need an explicit width and height (set in styles). */}
      <Image source={{ uri: `${BASE}/photo1.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>TODO: More detail text.</Text>

      <Image source={{ uri: `${BASE}/photo2.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>TODO: More detail text.</Text>

      <Image source={{ uri: `${BASE}/photo3.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>TODO: Closing text.</Text>
    </ScrollView>
  );
}