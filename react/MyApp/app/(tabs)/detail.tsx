import { ScrollView, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

const BASE = 'https://cs-people.bu.edu/atruong4/images';

export default function DetailScreen() {
  return (
    <ScrollView contentContainerStyle={styles.scrollContainer}>
      <Text style={styles.titleText}>My Hobbies</Text>

      <Text style={styles.bodyText}>One of my favorite hobbies is to watch NBA Games. NBA Games are so entertaining as you never know what can happen. One of my favorite team is a Boston Celtics as their team is filled with great players with good hustle. Paul George is my favorite player in the 2010's as his ability to be so smooth is great!</Text>

      <Image source={{ uri: `${BASE}/Picture of Me.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>Here's a picture of Paul George. He played on many different team including the Pacers, Clippers, Sixers and now Celtics. Even though he is older, he can still contribute a lot while providing good on ball defense</Text>

      <Image source={{ uri: `${BASE}/dasd.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>Here's another of my favorite team, the Knicks. The knicks had just won the NBA Championship and this was only possible by Jalen Brunson. He is a fantastic leader and know how to lead a team to victory. After 53 years since the last time the Knicks won the Championship, the Knicks celebrates this victory with all the different generations of fans who have been waiting for this moment.</Text>

      <Image source={{ uri: `${BASE}/images.jpg` }} style={styles.remoteImage} />

      <Text style={styles.bodyText}>Would love to connect to anyone also is a big fan!</Text>
    </ScrollView>
  );
}