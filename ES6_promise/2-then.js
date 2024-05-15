export default function handleResponseFromAPI(promise) {
  const promiseBody = {
    status: 200,
    body: 'success',
  };
  return promise
    .then(() => promiseBody)
    .catch((e) => e)
    .finally(() => console.log('Got a response from the API'));
}
