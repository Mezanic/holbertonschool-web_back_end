export default function getListStudentIds(arrayObject) {
  if (!Array.isArray(arrayObject)) return [];
  return arrayObject.map((value) => value.id);
}
