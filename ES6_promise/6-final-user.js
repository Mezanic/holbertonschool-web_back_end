/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => {
      results.map((result) => {
        let value;
        if (result.status === 'fulfilled') {
          value = result.value;
        } else {
          value = result.reason;
        }
        return {
          status: result.status,
          value,
        };
      });
    });
}
