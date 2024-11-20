export default function getListStudentIds(arrayObject, location) {
  return arrayObject.map((value) => value.location === location);
}
