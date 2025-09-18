from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="選單名稱")
    url = models.CharField(max_length=200, verbose_name="連結（/path 或完整網址）")
    parent = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name="父選單"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="排序（小到大）")
    is_active = models.BooleanField(default=True, verbose_name="啟用")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "選單"
        verbose_name_plural = "選單"

    def __str__(self):
        return self.title

    @property
    def active_children(self):
        """回傳啟用中的子選單"""
        return self.children.filter(is_active=True)