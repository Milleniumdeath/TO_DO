<script>
function confirmDelete(event) {
  event.preventDefault(); // havolani to‘xtat
  const deleteUrl = event.currentTarget.href;

  if (confirm("🛑 Rostdan ham ushbu topshiriqni o‘chirmoqchimisiz?")) {
    window.location.href = deleteUrl; // Ha bossa — o‘chirishga o't
  } else {
    window.location.href = "/"; // Yo'q bossa — bosh sahifaga qayt
  }

  return false;
}
</script>
