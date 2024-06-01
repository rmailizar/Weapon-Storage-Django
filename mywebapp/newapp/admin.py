from django.contrib import admin
from .models import member, weapon, RiwayatStok

class memberAdmin(admin.ModelAdmin):
    list_display="firstname", "lastname", "country"
    
class weaponAdmin(admin.ModelAdmin):
    list_display = "nama", "tipe", "jumlah"
    
class RiwayatStokAdmin(admin.ModelAdmin):
    list_display = ('get_weapon_name', 'get_weapon_tipe', 'waktu', 'jumlah_perubahan', 'jenis_perubahan')
    
    def get_weapon_name(self, obj):
        return obj.weapon.nama
    get_weapon_name.short_description = 'Weapon Name'
    
    def get_weapon_tipe(self, obj):
        return obj.weapon.tipe
    get_weapon_tipe.short_description = 'Weapon Type'
    
admin.site.register(member, memberAdmin)
admin.site.register(weapon, weaponAdmin)
admin.site.register(RiwayatStok, RiwayatStokAdmin)
