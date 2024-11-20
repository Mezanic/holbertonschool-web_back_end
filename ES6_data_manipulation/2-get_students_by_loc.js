export default function getListStudentIds(arrayObject, city) {
  return arrayObject.filter((value) => value.location === city);
}
