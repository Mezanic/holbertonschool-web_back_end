export default function uploadPhoto(filename) {
  const eslintapprouver = `${filename} cannot be processed`;
  return Promise.reject(new Error(eslintapprouver));
}
