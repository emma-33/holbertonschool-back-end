import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const p1 = await signUpUser(firstName, lastName)
    .then((data) => ({
      status: 'fulfilled',
      value: data,
    }));
  const p2 = await uploadPhoto(filename)
    .catch((error) => ({
      status: 'rejected',
      value: error.toString(),
    }));
  return [p1, p2];
}
